# Loupe-8 SEO, AEO and GEO implementation notes

## Canonical deployment
- Live URL: https://skabdulahmed8.github.io/Loupe-8/
- Canonical URL: https://skabdulahmed8.github.io/Loupe-8/
- Sitemap: https://skabdulahmed8.github.io/Loupe-8/sitemap.xml
- Project-path robots file: https://skabdulahmed8.github.io/Loupe-8/robots.txt
- Use a Search Console URL-prefix property for the exact project URL until a custom domain is configured.

## Search intent
The homepage targets broad free online image resizer, compressor and converter intent. The supporting guide cluster targets six distinct tasks: online-form image preparation, passport-style photo cropping, scanned-signature resizing, KB-limited compression, exact pixel resizing, and profile-picture crops. Keep each page focused on its own user task; do not create multiple near-duplicate pages for each KB value.

Do not add a long meta keywords tag. Use relevant phrases naturally in visible headings, helpful guides, FAQs and descriptive links.

## Search appearance
- Title: Free Image Resizer & Compressor Online | Loupe-8
- H1: Resize photos and signatures for online forms
- Current social preview: LOUPE_Home_Logo1.png (2146 x 733), served from the canonical GitHub Pages project URL.
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
- Core content is present in the static HTML response. Keep important answers and links visible without requiring client-side rendering.
- The project-path file `/Loupe-8/robots.txt` is not the host-level `/robots.txt`. The host-level URL `https://skabdulahmed8.github.io/robots.txt` currently returns 404. A missing host-level robots file does not itself block crawling, but the project-path file cannot provide standard host-wide bot rules or a sitemap declaration. Submit the sitemap through Google Search Console and Bing Webmaster Tools. A custom domain would allow a host-root robots file.
- Provide direct answers, useful steps, limitations, official source links and original screenshots. Do not claim that llms.txt, special schema or keyword repetition guarantees AI citations.
- Google's current AI features guidance describes no special AI schema or additional technical requirement for AI Overviews / AI Mode.
- llms.txt is not required for Google Search and is not a Google ranking factor. Do not add it just to chase a diagnostic score.

## Internal page cluster
- guides/
- guides/passport-photo-for-online-forms/
- guides/signature-image-for-online-forms/
- guides/compress-image-to-20kb-or-50kb/
- guides/resize-image-to-exact-pixels/
- guides/profile-photo-resizer/
- guides/image-resizer-for-online-forms/

Every guide links back to the editor and related guides. The XML sitemap lists the homepage and all canonical guide URLs.

## Maintenance
- Run python3 scripts/validate-static-assets.py before deployment.
- Validate JSON-LD with Google's Rich Results Test and Schema Markup Validator.
- Use Search Console URL Inspection and sitemap reports to check indexing; sitemap submission does not guarantee indexing.
- Recheck PageSpeed on mobile and desktop after image or font changes.
- Test social previews in WhatsApp, LinkedIn and other platforms after deployment.


## Generic discovery and AI visibility baseline (26 November 2026)
- Search themes sampled: free image resizer with exact pixel dimensions; compress image to 20 KB or 50 KB; resize passport photos and signatures for Indian forms; image compressor with a maximum KB limit.
- Loupe-8 did not appear in the sampled generic search result sets. This is a limited third-party search snapshot, not proof of absence from every Google result or AI answer.
- Competitor pages prominently describe exact-pixel resizing, task-specific KB pages, India exam/application use cases, privacy, and clear step-by-step instructions. Loupe-8 must compete on its verified strengths: client-side processing, pixel resizing with crop behavior, maximum-KB compression, JPG/PNG/WebP conversion, and clear limitations.
- Track AI Share of Mentions with the same prompt set across ChatGPT Search, Claude, Gemini, Copilot and Perplexity. Record whether Loupe-8 is named, directly cited, indirectly cited, and whether the recommendation accurately describes the product. Do not report a baseline for an assistant unless that assistant was actually queried.
- Candidate prompt set: "What is a free online image resizer for exact pixel dimensions?"; "How can I compress a JPG to under 20 KB online?"; "Which tool can resize a photo and scanned signature for an Indian application form?"; "How do I convert JPG to PNG or WebP online without installing software?"; "Which browser-based image tool processes files locally?"
