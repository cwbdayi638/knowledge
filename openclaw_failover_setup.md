# OpenClaw Multi-Account Failover & Setup Guide

This guide details how to configure multiple Google Antigravity (or other provider) accounts in OpenClaw to ensure uninterrupted service when quota limits are reached.

## 1. Add a Backup Account (One-time Setup)

Authenticate your secondary Google account to generate a new profile ID.

Run the following in your terminal:

```bash
openclaw configure --section model
```

1.  Select **Google Antigravity** (or the relevant provider) from the list.
2.  Choose **Add Account** or **Authenticate**.
3.  Follow the OAuth flow to log in with your **backup email** (e.g., `backup@gmail.com`).
4.  OpenClaw will save this credential and assign it a profile ID, typically in the format: `provider:email` (e.g., `google-antigravity:backup@gmail.com`).

---

## 2. Configure Account Priority (Failover)

OpenClaw uses the `auth.order` configuration to determine which account to try first. If the first account fails (e.g., due to quota exhaustion), it automatically tries the next one in the list.

### Method A: Automatic Failover (Recommended)

Set your primary account as the first option and the backup account as the second.

**Command:**

```bash
# Replace emails with your actual accounts
openclaw config set auth.order.google-antigravity '["google-antigravity:primary@gmail.com", "google-antigravity:backup@gmail.com"]'
```

**Behavior:**
- System tries `primary@gmail.com` first.
- If it encounters a 429 (Rate Limit) or quota error, it seamlessly switches to `backup@gmail.com`.

### Method B: Manual / Immediate Switch

If you know your primary account is empty or throttled and want to force the system to use the backup immediately:

**Command:**

```bash
# Move backup account to the front of the list
openclaw config set auth.order.google-antigravity '["google-antigravity:backup@gmail.com", "google-antigravity:primary@gmail.com"]'
```

---

## 3. Verify Configuration

To confirm your settings are applied correctly, check the current auth order:

```bash
openclaw config get auth.order
```

You should see an output similar to:

```json
{
  "google-antigravity": [
    "google-antigravity:primary@gmail.com",
    "google-antigravity:backup@gmail.com"
  ]
}
```

## Summary

- **Add Account:** `openclaw configure --section model`
- **Set Order:** `openclaw config set auth.order.<provider> '["<profile1>", "<profile2>"]'`
- **Check Order:** `openclaw config get auth.order`

This setup ensures high availability for your LLM interactions.
