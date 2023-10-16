# chatbot-intent
- 应用于对话机器人的意图识别服务
- 使用 elasticsearch 搜索引擎来完成服务。
- 这里在官方image的基础上制作了无密码版本的 elasticsearch image (elasticsearch_nopasswd_image.tar)

# 启动步骤
```
# 1. 启动 elasticsearch 服务
docker run -d --name elasticsearch  -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch_nopasswd:8.10.2
```