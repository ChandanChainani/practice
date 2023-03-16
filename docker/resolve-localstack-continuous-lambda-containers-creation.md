```sh
docker container ls -a \
  --format="{{.RunningFor}} {{.ID}}" \
  --filter ancestor=lambci/lambda:go1.18 | \
  grep 'minutes\|hours\|days' | \
  awk -F' ' '{ if ($1 > 2) print $4 }' | \
  xargs -r docker rm -f
```
