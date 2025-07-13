
# 🌐 Hosting Your 3D Uranium Visualization Online

## Quick Start Guide

### Prerequisites
- Your generated HTML file (e.g., `uranium_3d_map.html`)
- A GitHub account OR a Netlify account

---

## Method 1: GitHub Pages (Recommended)

### Step 1: Create GitHub Repository
1. Go to [GitHub.com](https://github.com) and sign in
2. Click "New repository" (green button)
3. Name it `uranium-visualization` (or any name you prefer)
4. Make sure it's **Public**
5. Check "Add a README file"
6. Click "Create repository"

### Step 2: Upload Your Files
1. Click "Upload files" in your repository
2. Drag and drop your HTML file
3. **Important**: Rename your file to `index.html` (GitHub Pages looks for this)
4. Add a commit message like "Add uranium 3D visualization"
5. Click "Commit changes"

### Step 3: Enable GitHub Pages
1. Go to repository **Settings** (top menu)
2. Scroll down to **Pages** section (left sidebar)
3. Under "Source", select "Deploy from a branch"
4. Choose "main" branch
5. Click "Save"

### Step 4: Access Your Live Site
- Your site will be available at: `https://yourusername.github.io/uranium-visualization/`
- It may take 5-10 minutes to go live initially

---

## Method 2: Netlify (Drag & Drop)

### Step 1: Prepare Your Files
1. Create a new folder on your computer
2. Copy your HTML file into it
3. **Important**: Rename to `index.html`

### Step 2: Deploy to Netlify
1. Go to [Netlify.com](https://netlify.com) and sign up
2. Click "Add new site" → "Deploy manually"
3. Drag your folder into the deployment area
4. Wait for deployment to complete

### Step 3: Customize Domain (Optional)
1. Click "Site settings" → "Domain management"
2. Click "Options" → "Edit site name"
3. Change to something like `uranium-visualization-punjab`
4. Your site will be at: `https://uranium-visualization-punjab.netlify.app/`

---

## Method 3: Netlify with GitHub (Continuous Deployment)

### Step 1: Push to GitHub
1. Follow GitHub method above but don't enable Pages
2. Just upload your files to GitHub repository

### Step 2: Connect to Netlify
1. Go to [Netlify.com](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Choose "GitHub" and authorize
4. Select your repository
5. Leave build settings as default
6. Click "Deploy site"

### Benefits:
- Automatic updates when you push changes to GitHub
- Custom domain support
- HTTPS enabled by default
- Better performance with CDN

---

## File Structure for Multi-Page Sites

If you have multiple visualizations, organize like this:

```
uranium-project/
├── index.html          # Main landing page
├── pydeck-map.html     # PyDeck visualization  
├── kepler-map.html     # Kepler.gl visualization
├── data/
│   └── uranium_data.csv
└── css/
    └── style.css
```

### Sample index.html for navigation:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Punjab Uranium Groundwater Analysis</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .nav { background: #f0f0f0; padding: 20px; border-radius: 5px; }
        .nav a { margin-right: 20px; text-decoration: none; color: #333; }
        .nav a:hover { color: #007bff; }
    </style>
</head>
<body>
    <h1>Punjab Uranium Groundwater Analysis</h1>
    <div class="nav">
        <a href="pydeck-map.html">PyDeck 3D Map</a>
        <a href="kepler-map.html">Kepler.gl Interactive Map</a>
        <a href="data/uranium_data.csv">Download Data</a>
    </div>
    <p>Select a visualization above to explore uranium concentrations in Punjab groundwater.</p>
</body>
</html>
```

---

## Custom Domain Setup (Optional)

### For GitHub Pages:
1. Buy a domain (e.g., from Namecheap, GoDaddy)
2. In your repository, go to Settings → Pages
3. Add your custom domain in "Custom domain" field
4. Update DNS settings with your domain provider:
   - Add CNAME record: `www` → `yourusername.github.io`
   - Add A records for root domain pointing to GitHub IPs

### For Netlify:
1. Go to Site Settings → Domain management
2. Click "Add custom domain"
3. Follow the DNS configuration instructions
4. Netlify provides automatic HTTPS certificates

---

## Troubleshooting

### Common Issues:
1. **Site not loading**: Check file is named `index.html`
2. **404 Error**: Verify repository is public and Pages is enabled
3. **Blank page**: Check browser console for JavaScript errors
4. **Maps not rendering**: Ensure internet connection for map tiles

### Performance Tips:
- Keep HTML files under 25MB for GitHub Pages
- Use CDN links for libraries instead of local files
- Optimize any images or data files
- Consider using relative paths for assets

---

## Security Considerations

### For Research Data:
- **Public repositories**: Anyone can see your data
- **Private repositories**: Use if data is sensitive (requires paid GitHub plan)
- **Data anonymization**: Remove sensitive location details if needed
- **Access control**: Use private repositories + GitHub Pages for team-only access

### Environment Variables:
If using Mapbox tokens:
```python
import os
# Use environment variables for sensitive keys
mapbox_token = os.getenv('MAPBOX_TOKEN', 'your-default-token')
```

---

## Next Steps

1. **Test your visualization** locally before deploying
2. **Choose your hosting method** (GitHub Pages recommended for beginners)
3. **Upload and configure** following the steps above
4. **Share your link** with colleagues or on social media
5. **Monitor usage** through GitHub/Netlify analytics

### Pro Tips:
- Use descriptive commit messages for version control
- Create a backup of your visualization files
- Consider adding a contact form or feedback mechanism
- Document your methodology and data sources on the page

Happy mapping! 🗺️
