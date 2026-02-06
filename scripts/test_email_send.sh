#!/bin/bash
# Test script for sending email with attachment

# Check if environment variables are set
if [ -z "$SENDER_EMAIL_NEW" ] || [ -z "$CWBDAYI_EMAIL_PASSWORD" ]; then
    echo "❌ Error: Email credentials not set!"
    echo ""
    echo "To test locally, set these environment variables:"
    echo "  export SENDER_EMAIL_NEW='your-email@gmail.com'"
    echo "  export CWBDAYI_EMAIL_PASSWORD='your-app-password'"
    echo ""
    echo "To use in GitHub Actions, add secrets in:"
    echo "  Repository Settings > Secrets and variables > Actions"
    exit 1
fi

# Test sending email with attachment
TO_EMAIL="oceanicdayi@gmail.com"
SUBJECT="Test Email with Attachment"
BODY="This is a test email sent from the knowledge repository."
ATTACHMENT="/workspaces/knowledge/README.md"

echo "📧 Sending test email to: $TO_EMAIL"
echo "📎 Attachment: $ATTACHMENT"

python3 /workspaces/knowledge/scripts/send_email_with_attachment.py \
    "$TO_EMAIL" \
    "$SUBJECT" \
    "$BODY" \
    "$ATTACHMENT"
