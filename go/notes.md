# For dynamic linked build
```go
go build -o main main.go
```

# For static linked build
```go
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -tags netgo -ldflags '-w -extldflags "-static"' -o main main.go
```

# For static linking of libcrypto and libssl
```go
go env -w GO111MODULE=on
GOOS=linux GOARCH=amd64 go build -a -ldflags='-linkmode external -extldflags "-ldl -static"' -o main main.go
```
