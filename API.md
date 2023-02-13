# API

Все запросы от бекенда фронтенду всегда будут в формате `json` и методом `POST`. Все ответы будут также ожидаться в
формате `json`.

Все эндпоинты, которые обслуживают потребности фронтенда будут начинаться с префикса `/frontend`.

Ответ от сервера всегда имеет стандартный вид:

* В случае успеха

    ```json
    {
      "status": "ok",
      "payload": {
        // payload fields
      }
    }
    ```

* В случае ошибки

    ```json
    {
      "status": "error",
      "error_info": {
        "name": "SomeErrorName",
        "details": {
          // error details 
        },
        "debug_message": "Debug string about error occurred"
      }
    }
    ```

`StatusCode` фронтендом игнорируется. Фронтенд сразу будет парсить тело ответа в `json` и если формат не будет
соответствовать, запрос будет воспринят как ошибочный.

# Endpoints

## Аутентификация

### Сущности

```typescript
interface AuthenticatedUser {
    login: string;
    name: string;
    email: string;
    phone?: string;
}
```

### Описание

* `/frontend/login` Логинит пользователя по логину и паролю. В случае неудачного логина возвращается
  ошибка `WrongLoginOrPassword`. В случае успеха пользователю должна вернуться валидная кука с информацией о
  пользователе.
* `/frontend/auth` Проводит первичную аутентификацию пользователя. Если пользователь уже залогинен, возвращает
  информацию о пользователе. Если не залогинен -- возвращает ошибку `NotAuthenticated`.
* `/frontend/sign_up` Регистрация пользователя по присланным данным. При успешной рагистрации тут же возвращает
  пользователю куку, как если бы он залогинился через `/frontend/login`.
* `/frontend/logout` Разлогинивает пользователя, удаляя информацию из кук.

### Формат запросов и ответов

```typescript
export interface Api {
    '/frontend/login': {
        request: {
            login: string;
            password: string;
        };
        response: AuthenticatedUser;
    };
    '/frontend/auth': {
        request: null;
        response: AuthenticatedUser;
    };
    '/frontend/sign_up': {
        request: {
            login: string;
            password: string;
            name: string;
            email: string;
        };
        response: AuthenticatedUser;
    };
    '/frontend/logout': {
        request: null;
        response: null;
    };
}
```
