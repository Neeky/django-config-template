# django-config-template

**django 方面的配置如下**

- [允许访问的主机](#允许访问的主机)
- [模板](#模板)
- [数据库](#数据库)
- [缓存](#缓存)
- [时区](#时区)
- [静态文件](#静态文件)
- [日志](#日志)

**webpack 方面的配置如下**


   ---

## 允许访问的主机
   ```python
   ALLOWED_HOSTS = ['*']
   ```
   ---

## 模板
   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
   
           # 全局模板
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```
   ---

## 数据库
   ```py
   # 使用 MySQL 的情况下可以用这个
   # DATABASES = {
   #    'default': {
   #        # 后台使用 MySQL 数据库
   #        'ENGINE': 'django.db.backends.mysql',
   #        # database 名
   #        'NAME': 'leorg',
   #        # 主机、端口、用户名、密码
   #        'HOST': '127.0.0.1',
   #        'PORT': 3306,
   #        'USER': 'tuser',
   #        'PASSWORD': 'euler'
   #    }
   # }
   
   # 使用 sqlite3
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
   }
   ```
   ---

## 缓存
   ```py
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
           'LOCATION': '/tmp/django-caches',
           'TIMEOUT': 3600,
       }
   }
   ```

   ---

## 时区
   ```py
   LANGUAGE_CODE = 'zh-hans'
   
   TIME_ZONE = 'Asia/Shanghai'
   
   USE_I18N = True
   
   USE_L10N = True
   
   USE_TZ = True
   ```

   ---

## 静态文件
   ```py
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, "static"),
   ]
   
   ```

## 日志
   ```py
   # 日志级别
   LOG_LEVEL = 'DEBUG' if DEBUG == True else 'INFO'
   
   # 日志配置
   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'formatters': {
           'simple': {
               'format': '{asctime} - {levelname} - {name} - {lineno} line - {message}',
               'style': '{',
           },
       },
       'handlers': {
           'file': {
               'level': LOG_LEVEL,
               'class': 'logging.handlers.RotatingFileHandler',
               'filename': '/tmp/django-apps.log',
               'formatter': 'simple',
               'maxBytes': 1024 * 1024 * 10,  # 10M
               'backupCount': 8
           },
           'console': {
               'level': 'INFO',
               'class': 'logging.StreamHandler',
               'formatter': 'simple'
           },
       },
       'loggers': {
           'django': {
               'handlers': ['console' if DEBUG == True else 'file'],
               'level': 'INFO',
               # 'propagate': True,
           },
           'apps': {
               'handlers': ['file'],
               'level': LOG_LEVEL,
               # 'propagate': True,
           }
       },
   }
   
   ```
   ---


# webpack

## webpack安装
```bash
npm install --save-dev webpack webpack-cli webpack-dev-server
npm install --save-dev babel-loader @babel/core @babel/preset-env style-loader css-loader vue-loader vue-template-compiler
npm install --save-dev html-webpack-plugin clean-webpack-plugin 

npm install --save vue
npm install axios
```