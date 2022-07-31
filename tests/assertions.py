class Assertions:
    @staticmethod
    def assert_keys_exists(keys, result):
        for key in keys:
            assert key in result, f"Key '{key} is not in result"

    @staticmethod
    def assert_key_value(result, key, value):
        assert result[key] == value, f"Key '{key}' value '{result[key]}' does not match {value}"