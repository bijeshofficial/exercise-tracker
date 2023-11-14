# EXERCISE TRACKER

App i am creating to track my workout progress based on my requirements.

## When the port is still being used

```bash
sudo lsof -t -i tcp:8000 | xargs kill -9
```

## Any change in the CSS

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```