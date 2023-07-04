# FastAPI simple base auth

Create creds
```shell
cat <<EOF> .env
export USER=admin
export PASSWORD=password
EOF
```

Run Docker container
```shell
docker-compose up -d
```

Check 
```shell
curl --request GET \
  --url http://localhost:8000/users/me \
  --header 'Authorization: Basic YWRtaW46cGFzc3dvcmQ='
```
