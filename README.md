# Flask-RESTful-API
使用 Python 的 Flask 框架实现一个简单的 RESTful 服务。

## 知识储备
1. HTTP 方法的含义与示例  

 HTTP方法 |   动作   |   示例   |  
---------|--------|---------|
GET|获取资源信息|http://example.com/api/resource
GET|获取资源信息|http://example.com/api/resource/123
POST|创建一个资源|http://example.com/api/resource
PUT|更新一个资源|http://example.com/api/resource/123
DELETE|删除一个资源|http://example.com/api/resource/123

2. API 返回的常见的 HTTP 状态码

HTTP状态码|名称|说明
---|---|---|
200|OK|请求成功完成
201|Created|请求成功地创建了一个新资源
400|Bad Request|请求不可用或不一致
401|Unauthorized|请求未包含认证信息
403|Forbidden|请求中发送的认证密令无权访问目标
404|Notfound|URL对应的资源不存在
405|Method not allowed|指定资源不支持请求使用的方法
500|Internal server error|处理请求的过程中发生意外错误

