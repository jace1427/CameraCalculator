cd frontend
npm install
npm run build
cd ..
npm install -g serve
serve -s frontend/build -l 80 --no-clipboard
