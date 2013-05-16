export DJANGO_SETTINGS_MODULE=djci.test_settings

./manage.py syncdb --noinput --verbosity 0

./manage.py runserver 8081 > /dev/null 2>&1 &
PID=$!

sleep 3

nosetests --nologcapture -s djci.tests_selenium
CODE=$?

pkill -TERM -P $PID
exit $CODE