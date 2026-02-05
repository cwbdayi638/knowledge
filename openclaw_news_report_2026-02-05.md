# OpenClaw Latest News Report (2026-02-05)

## Version: 2026.1.29 (Stable)

### Key Updates:
1.  **Rebranding**: Complete transition to the `openclaw` name, including the npm package, CLI, and extensions (now under `@openclaw/*`).
2.  **Security Hardening**:
    *   New Control UI device auth bypass flag for specialized setups.
    *   Enhanced security warnings for beta access.
    *   Gateway now requires token/password by default (auth mode "none" removed).
3.  **Browser Control**:
    *   Architecture shift: Browser control is now routed via the Gateway or Node proxies.
    *   Removed standalone browser control command for better integration.
4.  **Messaging Channel Improvements**:
    *   **Telegram**: Now supports quote replies, message editing, captions for media, and sticker vision caching.
    *   **Discord**: Added configurable privileged gateway intents for better presence/member tracking.
    *   **LINE**: New plugin support with rich and quick replies.
5.  **Memory & Agents**:
    *   Memory search now allows indexing extra paths.
    *   Compaction safeguard now summarizes dropped messages to prevent context loss.
6.  **Tooling**:
    *   Added per-sender group tool policies.
    *   Enhanced `exec` allowlist checks with `safeBins` support.

### System Status:
*   **Gateway**: Running locally on version 2026.1.29.
*   **Current Model**: `google-antigravity/gemini-3-flash`.
*   **Context Usage**: 411k tokens (Compactions active).

---
*Report generated on 2026-02-05 05:15 UTC*
