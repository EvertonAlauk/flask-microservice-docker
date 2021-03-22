
def test_app_bank_account_is_created(user_app):
    assert user_app.root_path.endswith('/bank_account/app')