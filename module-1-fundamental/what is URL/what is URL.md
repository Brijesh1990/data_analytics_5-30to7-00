# What is URL?

## Definition

A **URL** (Uniform Resource Locator) is the address used to access resources on the internet. It specifies the location of a resource (such as a webpage, image, or file) on a computer network and a mechanism for retrieving it.

### Key Characteristics
- **Unique**: Each URL is unique and points to a specific resource
- **Standardized**: URLs follow a standardized format defined by RFC 3986
- **Universal**: Works across all internet browsers and platforms
- **Hierarchical**: Organized in a hierarchical structure from general to specific

---

## URL Structure

A typical URL has the following components:

```
protocol://domain:port/path?query_string#fragment_id
```

### Components Breakdown

| Component | Example | Description |
|-----------|---------|-------------|
| **Protocol** | `https://` | The method used to access the resource (http, https, ftp, etc.) |
| **Domain/Host** | `www.example.com` | The server's address where the resource resides |
| **Port** | `:8080` | Optional port number (default: 80 for http, 443 for https) |
| **Path** | `/path/to/page` | The specific location of the resource on the server |
| **Query String** | `?key=value&name=john` | Optional parameters passed to the server |
| **Fragment** | `#section1` | Reference to a specific section within the page |

---

## Common URL Examples

### 1. **Web Pages**
- `https://www.google.com` - Google homepage
- `https://www.wikipedia.org/wiki/URL` - Wikipedia article about URLs
- `https://www.github.com` - GitHub repository hosting
- `https://www.amazon.com/s?k=laptop` - Amazon search results

### 2. **Email**
- `mailto:user@example.com` - Send email to a user
- `mailto:support@company.com?subject=Help` - Email with subject

### 3. **File Transfer**
- `ftp://files.example.com/documents/file.pdf` - FTP file access
- `sftp://secure.example.com/data/backup.zip` - Secure file transfer

### 4. **Social Media**
- `https://www.facebook.com/username` - Facebook profile
- `https://www.twitter.com/username` - Twitter profile
- `https://www.linkedin.com/in/username` - LinkedIn profile
- `https://www.instagram.com/username` - Instagram profile
- `https://www.tiktok.com/@username` - TikTok profile

### 5. **Video & Streaming**
- `https://www.youtube.com/watch?v=dQw4w9WgXcQ` - YouTube video
- `https://www.netflix.com` - Netflix streaming service
- `https://www.twitch.tv/username` - Twitch streaming channel

### 6. **Shopping & E-commerce**
- `https://www.ebay.com/itm/123456789` - eBay product listing
- `https://www.etsy.com/shop/shopname` - Etsy shop

### 7. **Cloud & Storage**
- `https://www.dropbox.com` - Dropbox cloud storage
- `https://www.onedrive.live.com` - Microsoft OneDrive
- `https://drive.google.com` - Google Drive

### 8. **Developer & Technical**
- `https://api.github.com/users/username` - GitHub API
- `https://stack.stackoverflow.com/questions/12345` - Stack Overflow Q&A
- `https://www.npm.js.com/package/packagename` - NPM package registry
- `https://pypi.org/project/packagename` - Python Package Index

### 9. **Documentation & Learning**
- `https://www.w3schools.com/html/` - W3Schools HTML tutorial
- `https://www.mdn.org/en-US/docs/web/` - Mozilla Developer Network
- `https://docs.python.org/3/` - Python official documentation

### 10. **Search Engines**
- `https://www.google.com/search?q=python+tutorial` - Google search
- `https://www.bing.com/search?q=web+development` - Bing search
- `https://www.duckduckgo.com/?q=privacy` - DuckDuckGo search

### 11. **News & Media**
- `https://www.bbc.com/news` - BBC News
- `https://www.cnn.com` - CNN News
- `https://www.reddit.com/r/programming` - Reddit programming community

### 12. **Banking & Finance**
- `https://www.paypal.com` - PayPal payment service
- `https://www.stripe.com` - Stripe payment processing
- `https://www.coinbase.com` - Cryptocurrency exchange

---

## URL Encoding

Special characters in URLs must be encoded using percent-encoding (URL encoding):

| Character | Encoded |
|-----------|---------|
| Space | `%20` or `+` |
| `#` | `%23` |
| `&` | `%26` |
| `=` | `%3D` |
| `?` | `%3F` |
| `/` | `%2F` |
| `:` | `%3A` |

**Example**: `https://www.example.com/search?q=hello%20world`

---

## URL Types by Protocol

| Protocol | Full Name | Purpose | Default Port |
|----------|-----------|---------|---------------|
| `http://` | HyperText Transfer Protocol | Web pages (unencrypted) | 80 |
| `https://` | HyperText Transfer Protocol Secure | Web pages (encrypted) | 443 |
| `ftp://` | File Transfer Protocol | File transfer | 21 |
| `sftp://` | SSH File Transfer Protocol | Secure file transfer | 22 |
| `mailto:` | Mail Protocol | Email composition | N/A |
| `tel:` | Telephone Protocol | Phone calls | N/A |
| `file://` | File Protocol | Local files | N/A |
| `ws://` | WebSocket | Real-time communication | 80 |
| `wss://` | WebSocket Secure | Secure real-time communication | 443 |

---

## Best Practices for URLs

1. **Keep URLs short and descriptive** - Use meaningful names that describe content
2. **Use lowercase letters** - Avoid inconsistencies
3. **Avoid special characters** - Use hyphens instead of underscores
4. **Use HTTPS** - Always prefer secure connections
5. **Avoid query strings in static URLs** - Use clean URLs when possible
6. **Make URLs readable** - Easy to understand and remember
7. **Use appropriate domain names** - Reflect your business or content

---

## Related Concepts

- **URI (Uniform Resource Identifier)** - Broader term that includes URLs
- **Domain Name** - The human-readable address of a website
- **IP Address** - The numerical address of a server (e.g., 192.168.1.1)
- **DNS (Domain Name System)** - System that translates domain names to IP addresses
- **Web Browser** - Software used to access and display web pages via URLs
