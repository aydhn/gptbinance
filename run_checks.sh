poetry run black app/performance_plane/ app/main.py tests/test_performance_plane*.py
poetry run flake8 app/performance_plane/ app/main.py tests/test_performance_plane*.py --ignore=E501
