1.JWT TOKEN [JSON WEB TOKEN]

Authentication 
Authorization 

JSON:  data format 
web: used for web/api communication 
token: authentication/authorization 

header : stores meta data (token type - jwt, algorithm -H256)
payload : stores users data or token data (user_id, username)
signature : (combination of header and payload ) + (signature): verify the token and user

authentication(username + password)

access token: short time live (protected )
refresh token: longer-lived credential used to obtain a new access token without requiring the user to log in again. 

Permission:
AllowAny
ISAuthenticated
