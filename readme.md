# FastAPI MongoDB User Management API

This is a FastAPI-based API for user and organization management using MongoDB.

## Setup
- Clone the repository
- Install the required packages by running pip install -r requirements.txt
- Start the API server by running uvicorn main:app --reload
- The API will be available at http://localhost:8000.

## Endpoints
- GET /users - Get all users
- POST /users - Create a new user
- GET /users/{user_id} - Get a user by id
- POST /orgs - Create a new organization
- GET /orgs - Get all organizations
- POST /user_orgs - Add a user to an organization
- DELETE /user_orgs - Remove a user from an organization

## Collections
- users
- orgs
- user_orgs

## License
[MIT](/LICENSE)

## Author
[Narayan Soni](https://github.com/narayan954)

## Credits
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)

[1]: https://fastapi.tiangolo.com/
[2]: https://www.mongodb.com/
[3]: https://pydantic-docs.helpmanual.io/
[4]: https://www.uvicorn.org/
[5]: https://github.com/narayan954
