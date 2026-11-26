# Loupe-8 SEO, AEO and GEO implementation notes

## Canonical deployment
- Live URL: https://skabdulahmed8.github.io/Loupe-8/
- Canonical URL: https://skabdulahmed8.github.io/Loupe-8/
- Sitemap: https://skabdulahmed8.github.io/Loupe-8/sitemap.xml
- Project-path robots file: https://skabdulahmed8.github.io/Loupe-8/robots.txt
- Use a Search Console URL-prefix property for the exact project URL until a custom domain is configured.

## Search intent
The homepage targets image resizer and compressor intent. Supporting guides target five distinct tasks: passport-style photo cropping, scanned-signature resizing, KB-limited compression, exact pixel resizing, and profile-picture crops.

Do not add a long meta keywords tag. Use relevant phrases naturally in visible headings, helpful guides, FAQs and descriptive links.

## Search appearance
- Title: Free Image Resizer & Compressor Online | Loupe-8
- H1: Resize photos and signatures for online forms
- Current social preview: LOUPE_Home_Logo1.png (2146 x 733), served from the repository's raw GitHub URL.
- The current image is a wide logo asset, not a dedicated 1200 x 630 preview. A purpose-built social image remains a future asset improvement.
- Keep canonical, Open Graph URL, Twitter image, sitemap and page URL aligned.
- Google may rewrite title links, snippets, favicons and site labels; metadata does not guarantee an exact display.
- Google does not support a separate site name for a GitHub Pages project subdirectory. A custom domain is the longer-term brand-identity improvement.

## Structured data
- Homepage: WebSite, Organization and WebApplication.
- Guide articles: Article and visible BreadcrumbList.
- Guide index: CollectionPage.
- Do not add aggregateRating: local browser ratings are not public, verifiable aggregates.
- Do not add FAQPage expecting Google FAQ rich results; Google discontinued that rich-result feature.
- Structured data must match visible page content.

## India-first accuracy
- No one photo ratio, file-size range, DPI or pixel dimension applies to every government application.
- The Passport 35:45 option is a crop ratio, not proof that an image meets a particular passport or recruitment workflow.
- Link to official instructions and re-check them before publishing numerical limits.
- The UPSC online application FAQ contains one current photo/signature example; it is not a universal standard for SSC, Passport Seva or other portals.

## Privacy and trust
- State that selected images are processed in the browser and are not uploaded to a Loupe image-processing server.
- Do not claim that no data is transmitted anywhere: the page loads Google Fonts and the hosting provider may retain standard server logs.
- Ratings and reviews remain in the current browser and are not public testimonials.

## AI search
- Keep core content in the delivered HTML.
- Allow search and answer-engine crawlers unless a deliberate privacy or licensing decision changes that policy.
- Provide direct answers, useful steps, limitations, source links and original screenshots.
- Google's current AI features guidance describes no special AI schema or additional technical requirement for AI Overviews / AI Mode.
- llms.txt is not required for Google Search and is not a Google ranking factor. Do not add it just to chase a diagnostic score.

## Internal page cluster
- guides/
- guides/passport-photo-for-online-forms/
- guides/signature-image-for-online-forms/
- guides/compress-image-to-20kb-or-50kb/
- guides/resize-image-to-exact-pixels/
- guides/profile-photo-resizer/

Every guide links back to the editor and related guides. The XML sitemap lists the homepage and all canonical guide URLs.

## Maintenance
- Run python3 scripts/validate-static-assets.py before deployment.
- Validate JSON-LD with Google's Rich Results Test and Schema Markup Validator.
- Use Search Console URL Inspection and sitemap reports to check indexing; sitemap submission does not guarantee indexing.
- Recheck PageSpeed on mobile and desktop after image or font changes.
- Test social previews in WhatsApp, LinkedIn and other platforms after deployment.
