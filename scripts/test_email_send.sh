#!/bin/bash
# Test script for sending email with attachment

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

SENDER_EMAIL_NEW="${SENDER_EMAIL_NEW:-$EMAIL_TO}"
CWBDAYI_EMAIL_PASSWORD="${CWBDAYI_EMAIL_PASSWORD:-$EMAIL_PASSWORD}"

# Check if environment variables are set
if [ -z "$SENDER_EMAIL_NEW" ] || [ -z "$CWBDAYI_EMAIL_PASSWORD" ]; then
    echo "⚠️  Skipping email send test: credentials not set."
    echo ""
    echo "To test locally, set one of these environment variable pairs:"
    echo "  export SENDER_EMAIL_NEW='your-email@gmail.com'"
    echo "  export CWBDAYI_EMAIL_PASSWORD='your-app-password'"
    echo ""
    echo "  export EMAIL_TO='your-email@gmail.com'"
    echo "  export EMAIL_PASSWORD='your-app-password'"
    echo ""
    echo "To use in GitHub Actions, add secrets in:"
    echo "  Repository Settings > Secrets and variables > Actions"
    exit 0
fi

# Test sending email with attachment
TO_EMAIL="oceanicdayi@gmail.com"
SUBJECT="Test Email with Attachment"
BODY="This is a test email sent from the knowledge repository."
ATTACHMENT="$REPO_ROOT/README.md"

echo "📧 Sending test email to: $TO_EMAIL"
echo "📎 Attachment: $ATTACHMENT"

python3 "$SCRIPT_DIR/send_email_with_attachment.py" \
    "$TO_EMAIL" \
    "$SUBJECT" \
    "$BODY" \
    "$ATTACHMENT"
