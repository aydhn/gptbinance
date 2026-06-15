echo "Integrations:"
grep -r 'RELIANCE PLANE INTEGRATION' app/*_plane/ | wc -l
echo "CLI integrations:"
grep -A 5 'RELIANCE PLANE CLI' app/main.py
