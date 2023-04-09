docker build --platform linux/amd64 -t chat_pt .
docker tag chat_pt:latest 563542513526.dkr.ecr.ap-northeast-2.amazonaws.com/chat_pt:arm
docker push 563542513526.dkr.ecr.ap-northeast-2.amazonaws.com/chat_pt:arm