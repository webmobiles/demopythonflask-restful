echo  "api code: ${MAILJET_API_KEY}:${MAILJET_API_SECRET}"
curl -s -X POST --user "${MAILJET_API_KEY}:${MAILJET_API_SECRET}" https://api.mailjet.com/v3.1/send -H "Content-Type: application/json" -d @a.json
