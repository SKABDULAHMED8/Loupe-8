# Loupe-8 SEO, AEO and GEO implementation notes

## Canonical deployment
- Live URL: https://skabdulahmed8.github.io/Loupe-8/
- Canonical URL: https://skabdulahmed8.github.io/Loupe-8/
- Sitemap: https://skabdulahmed8.github.io/Loupe-8/sitemap.xml
- Project-path robots file: https://skabdulahmed8.github.io/Loupe-8/robots.txt
- The actual website is a GitHub Pages project site beneath the `/Loupe-8/` path. The host root `https://skabdulahmed8.github.io/` currently returns 404.
- The project-path `robots.txt` is not the host-level robots file. A host-level robots file must be served from `https://skabdulahmed8.github.io/robots.txt`; it cannot be supplied from inside this project path.
- The host root currently returns 404 for `robots.txt`, which means there is no explicit host-level robots policy to edit from this repository. Do not assume the project-path file controls OpenAI, Anthropic, Perplexity, Bing or Google crawler access at the host level.
- Use a Google Search Console URL-prefix property for the exact project URL. Submit the sitemap URL listed above and inspect the homepage and guide URLs individually.
- Add the exact project URL to Bing Webmaster Tools as well. Check Bing's AI Performance report when available; it reports citations from Copilot and Bing AI answers, not Google rankings.
- A separate user-site repository or custom domain would be required to control the hostname root and publish a host-level `robots.txt`. That is outside this repository's scope and needs a separate decision.


## Google Search Central SEO Starter Guide baseline

Treat Google's own documentation as the primary standard for Google Search. The current implementation should follow these rules:

- Publish useful, original, accurate and maintained content for people. Each guide must solve a distinct image-preparation task; do not create near-duplicate keyword pages.
- Use one descriptive, page-specific title element, one clear H1 and a concise, page-specific meta description. Google may generate a different title link or snippet from visible page content; metadata does not guarantee exact wording or ranking.
- Keep each page's canonical URL aligned with its Open Graph URL and sitemap entry. Keep internal navigation as normal crawlable anchor links with descriptive link text.
- Add descriptive alt text to meaningful images. Keep key explanatory text, limitations and practical steps in HTML that a crawler can access.
- Use structured data only when it accurately describes visible page content. Valid JSON-LD can make a page eligible for supported search features, but it does not guarantee a rich result.
- Do not add a meta-keywords tag: Google Search does not use it. Do not repeat target phrases unnaturally or add blocks of keyword variants. Google's guide specifies no magic minimum or maximum word count for ranking.
- Use the sitemap as a discovery aid containing the preferred canonical URLs. It is optional and does not guarantee crawling or indexing. This project currently has nine canonical URLs; do not replace them with only the homepage.
- Use Search Console's URL Inspection to distinguish the live page test from the indexed version. Use the Sitemaps report to check whether the sitemap was already submitted and fetched before submitting it again.

Primary references:
- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Google spam policies: keyword stuffing](https://developers.google.com/search/docs/essentials/spam-policies#keyword-stuffing)
- [Google: crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- [Search Console URL Inspection](https://support.google.com/webmasters/answer/9012289/)

## Search intent and page map
The homepage targets the broad category "free online image resizer" and explains exact pixel dimensions, maximum KB limits and image-format conversion.

Supporting guides target different tasks:
- Passport-style photo cropping for online forms.
- Resizing an existing scanned signature.
- Compressing JPG or WebP to a maximum KB value such as 20 KB or 50 KB.
- Resizing an image to exact pixel width and height.
- Cropping and resizing a profile picture.
- Resizing and compressing an image for an online form in one workflow.
- Converting images to JPG, PNG or WebP, including transparency and GIF limitations.

Avoid publishing many near-identical keyword pages. Each guide must solve a distinct task, include accurate tool behavior, and link to the editor and related guides.

## Primary search appearance
- Homepage title: Free Online Image Resizer & Compressor | Loupe-8
- Homepage H1: Free online image resizer for exact pixels and KB limits
- Description: Resize images to exact pixel dimensions, crop photos, compress JPG or WebP to a maximum KB limit, and convert JPG, PNG and WebP in your browser. Free, no signup.
- Keep canonical, Open Graph URL, Twitter image, sitemap and page URL aligned.
- Google may rewrite title links, snippets, favicons and site labels. Metadata does not guarantee an exact display.
- The current social preview uses `LOUPE_Home_Logo1.png` at 2146 x 733. It is a wide logo asset, not an ideal dedicated 1200 x 630 share card. A purpose-built share image remains a follow-up improvement.
- Google does not support a separate site name for a GitHub Pages project subdirectory. A custom domain is the longer-term brand-identity improvement.

## Structured data
- Homepage: WebSite, Organization and WebApplication.
- Guide articles: Article and visible BreadcrumbList.
- Guide index: CollectionPage.
- Do not add aggregateRating: local browser ratings are not public, verifiable aggregates.
- Do not add FAQPage expecting Google FAQ rich results; structured data must match visible page content.
- Do not add fake reviews, unsupported "best" claims or universal acceptance promises.
- Structured data helps describe the visible page; it does not guarantee a rich result or AI citation.

## India-first accuracy
- No one photo ratio, file-size range, DPI or pixel dimension applies to every government application.
- The Passport 35:45 option is a crop ratio, not proof that an image meets a particular passport or recruitment workflow.
- The Resize tool keeps the requested pixel dimensions when its maximum JPG size can be met; if it cannot, it reports the size-limit problem.
- The separate Compress tool can reduce image dimensions when needed to meet a maximum KB value.
- Minimum JPG size padding adds non-image data and does not improve visible quality. Do not promise acceptance by a portal that may reject the added data.
- JPG exports use a white background for transparent image areas. GIF inputs are processed as still images.
- Loupe writes selected DPI metadata to JPG files only. Do not state that DPI is applied to PNG or WebP.
- Link to official instructions and re-check them before publishing numerical limits.
- The UPSC online application FAQ contains one application-specific example; it is not a universal standard for SSC, Passport Seva or other portals.

## Privacy and trust
- State that selected images are processed in the browser and are not uploaded to a Loupe image-processing server.
- Do not claim that no data is transmitted anywhere: the page loads Google Fonts and the hosting provider may retain standard server logs.
- Ratings and reviews remain in the current browser and are not public testimonials.
- Do not suggest users upload sensitive identity images to a third-party alternative.

## AI search and answer-engine readiness
- Keep important explanatory content in the delivered HTML, not only in JavaScript-generated UI.
- Provide direct answers, task steps, limitations, tables, official source links and original product evidence.
- Allow search and answer-engine crawlers unless an explicit privacy or licensing decision requires restrictions. Current host-level crawler directives cannot be controlled from this project subdirectory alone.
- Google's AI features guidance says standard SEO fundamentals apply; it does not require special AI schema or a separate AI-optimized page.
- `llms.txt` is not required for Google Search and is not a Google ranking factor. Do not add it only to improve a diagnostic score.
- OpenAI documents OAI-SearchBot as its search crawler; Anthropic documents Claude-SearchBot for search; Perplexity and Bing publish crawler and webmaster guidance. Those policies use the host-level robots path.
- No crawler setting can guarantee inclusion, recommendation or citation from ChatGPT, Claude, Gemini, Copilot or Perplexity.

## Internal page cluster
- `guides/`
- `guides/passport-photo-for-online-forms/`
- `guides/signature-image-for-online-forms/`
- `guides/compress-image-to-20kb-or-50kb/`
- `guides/resize-image-to-exact-pixels/`
- `guides/profile-photo-resizer/`
- `guides/resize-and-compress-image-for-online-form/`
- `guides/convert-image-to-jpg-png-webp/`

Every guide links back to the editor and related guides. The XML sitemap lists the homepage, guide index and all canonical guide URLs.

## Maintenance and measurement
- Run `python3 scripts/validate-static-assets.py` before deployment.
- Validate JSON-LD with Google's Rich Results Test and Schema Markup Validator.
- Use Search Console URL Inspection to check crawling, indexing and the selected canonical. A sitemap is a discovery hint, not a guarantee of indexing.
- Submit the XML sitemap in Search Console and Bing Webmaster Tools. IndexNow needs a verified key and does not replace sitemap submissions.
- Record baseline generic queries such as:
  - free online image resizer
  - resize image to exact pixels
  - resize image to exact size
  - compress image to 20 KB
  - compress photo for online form
  - resize and compress image for an online form
  - convert image to JPG, PNG or WebP
- Track impressions, clicks and average position in Search Console by query and page. For AI platforms, track citations and referred visits separately. Do not infer traffic or ranking from a single search snapshot.
- Recheck PageSpeed on mobile and desktop after image or font changes.
- Test social previews in WhatsApp, LinkedIn and other platforms after deployment.
