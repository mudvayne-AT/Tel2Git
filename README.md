<div align="center">

# Telegram Downloader
**Huge thanks to [nscl5/sandbox](https://github.com/nscl5/sandbox) for doing the heavy lifting**

### 🔗 **[Click here to see your Download Links](./Links.md)**

</div>

---

## 🚀 Features
* **Bypass Restrictions:** Download from channels/groups even if "Forwarding/Saving" is restricted by the owner.
* **Smart Split:** Automatically split large videos/audios into playable segments (MP4, MKV, MP3, etc.) instead of boring ZIP files.
* **Large File Support:** Uses ZIP splitting for non-media files or if you prefer a password-protected archive.
* **Direct Links:** Get clean, direct GitHub raw links to your files once processed.

---

## 🛠️ Initial Setup (Do this once)

### 1. Fork & Permissions
1. **Fork** this repository to your own account.
2. Go to your fork's **Settings** > **Actions** > **General**.
3. Under **Workflow permissions**, select **Read and write permissions** and click **Save**.

### 2. Get Telegram API Credentials
1. Log in to [my.telegram.org](https://my.telegram.org/auth?to=apps).
2. Go to **API development tools** and create an app (name it anything).
3. Copy your `API_ID` and `API_HASH`.

### 3. Generate your Session String
Since this workflow runs on **your account**, you need a session string:
1. Open the file `stringsession.py` in this repo.
2. Replace the `API_ID` and `API_HASH` with your own values.
3. Run the script: `python stringsession.py`
4. Log in as prompted. The script will print a long string of characters. **Copy this string.**

### 4. Set up GitHub Secrets
Go to your repo **Settings** > **Secrets and variables** > **Actions** and add these three **Repository secrets**:

| Name | Value |
| :--- | :--- |
| `API_ID` | Your ID (e.g., `4123213`) |
| `API_HASH` | Your Hash (e.g., `a21bcedeaf44...`) |
| `SESSION_STRING` | The long string from step 3 |

> [!IMPORTANT]
> **Do NOT use quotation marks** (`"` or `'`) when pasting the values into the secret fields.

---

## 📥 How to Download

### 1. Get the Link
The script accepts links in these formats:
* **Public:** `https://t.me/username/123`
* **Private:** `https://t.me/c/1234567/123`

**Tip:** If you want to download from a private chat, bot, or your "Saved Messages," simply forward the message to a private channel/group you created and use that message link!

### 2. Run the Workflow
1. Go to the **Actions** tab in your GitHub repo.
2. Select **Telegram Downloader** from the left sidebar.
3. Click the **Run workflow** dropdown button.
4. Paste your **Telegram Link**.
5. Choose your **Large File Handling** mode:
   * **Default ZIP:** Good for any file.
   * **Smart Split:** Best for videos/audio (keeps them playable).
6. Click **Run workflow**.

Once finished, your links will appear in the [Links.md](./Links.md) file!

---

> [!WARNING]  
> This tool is for personal use. Your `SESSION_STRING` is like a password to your account; never share it or post it publicly.
