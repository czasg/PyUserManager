# # coding: utf-8
# import pywss
# import sqlalchemy
# import src.initialize
# import src.api
#
#
# def sqlalchemy_engine():
#     return sqlalchemy.create_engine(
#         "postgresql://scott:tiger@localhost/test",
#         pool_size=3,
#         pool_recycle=3600,
#         pool_pre_ping=True,
#         pool_use_lifo=True,
#         echo_pool=True
#     )
#
#
# if __name__ == '__main__':
#     app = pywss.App()
#     engine = sqlalchemy_engine()
#     src.initialize.Initialize(app, engine)
#     app.run()


import loggus
import logging
import casbin
import casbin_sqlalchemy_adapter


# Use SQLAlchemy Casbin adapter with SQLLite DB
adapter = casbin_sqlalchemy_adapter.Adapter('sqlite:///test.db')

# Create a config model policy
with open("rbac_example_model.conf", "w") as f:
    f.write("""
    [request_definition]
    r = sub, obj, act

    [policy_definition]
    p = sub, obj, act

    [policy_effect]
    e = some(where (p.eft == allow))

    [matchers]
    m = r.sub == p.sub && r.obj == p.obj && r.act == p.act
    """)
with open("rbac_example_policy.csv", "w") as f:
    f.write("""
p, alice, data1, read
p, bob, data2, write
p, data2_admin, data2, read
p, data2_admin, data2, write
g, alice, data2_admin
    """)

# Create enforcer from adapter and config policy
e = casbin.Enforcer('rbac_example_model.conf', adapter)
# e = casbin.Enforcer('rbac_example_model.conf', "rbac_example_policy.csv")
e.logger.setLevel(logging.FATAL)
sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"
e.add_role_for_user('zhangsan', 'admin')

if e.enforce(sub, obj, act):
    print("permit alice to read data1")
else:
    print("deny the request, show an error")