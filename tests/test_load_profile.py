from src.load_profile import parse_args


def test_parse_args_defaults(monkeypatch):
    monkeypatch.setattr("sys.argv", ["load_profile.py"])
    args = parse_args()
    assert args.users == 1
    assert args.requests == 20
