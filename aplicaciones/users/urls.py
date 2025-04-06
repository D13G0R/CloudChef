from django.urls import path
from aplicaciones.users.views import index, register, loginUser, Signout, addUser, editUser, deleteUser, registerEnterprise


urlpatterns = [
    path("adminUsers/", index.as_view(), name="adminUsers"),

    path("adminUsersAdd/", addUser.as_view(), name = "adminUserAdd"),
    path("adminUserEdit/<int:pk>", editUser.as_view(), name = "adminUserEdit"),
    path("adminUserDelete/<int:pk>", deleteUser.as_view(), name = "adminUserDelete"),

    path("registerEnterprise/", registerEnterprise.as_view(), name = "registerEnterprise"),

    path("register/", register.as_view(), name="register"),
    path("loginUser/", loginUser.as_view(), name="loginUser"),
    path("logout/", Signout, name="SignOut"),
]
