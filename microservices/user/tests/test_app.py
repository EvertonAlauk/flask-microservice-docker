
def test_app_user_is_created(user_app):
    assert user_app.root_path.endswith('/user/app')