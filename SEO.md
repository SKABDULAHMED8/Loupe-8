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

## Google Search Console: generative AI control

Google provides a separate **Search generative AI control** in Search Console settings. It manages whether a site's content can be used for grounding or displayed with links in Google Search generative AI features such as AI Overviews and AI Mode.

- For Loupe-8, keep this control set to allow inclusion if the goal is to appear as a supporting source in Google AI Search features.
- This setting is separate from ordinary Google Search ranking. Changing it does not improve or reduce standard blue-link rankings.
- Keep Googlebot crawling allowed and pages indexable. A page must still be indexed and eligible for a Search snippet before it can be considered for Google AI Search features.
- Do not confuse this setting with `Google-Extended`. Google documents `Google-Extended` as a control for model training and grounding on non-Search generative AI products; it is not the switch for appearing in AI Overviews or AI Mode.
- This is an account-level Search Console setting. Repository code cannot enable it on the owner's behalf.

Official control details: https://developers.google.com/search/docs/fundamentals/gen-ai-controls

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

## Official SEO, AEO and GEO alignment

Use primary search-engine documentation as the standard. Do not treat third-party GEO scores, keyword-density scores or AI-citation promises as ranking evidence.

- Google SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google Search Essentials: https://developers.google.com/search/docs/essentials
- Google AI features and your website: https://developers.google.com/search/docs/appearance/ai-features
- Google generative AI optimization guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google crawlable link guidance: https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- Bing Webmaster Guidelines: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a

Implementation rules:
- Keep one descriptive, accurate title, one H1, a unique meta description and one self-referencing canonical URL on each indexable page.
- Keep the important product explanation, FAQs, limitations and guide content in crawlable HTML. Do not rely on a JavaScript-only text layer for the main explanation.
- Use ordinary anchor elements with useful link text to connect the homepage, guide index and individual guides.
- Keep visible page content and JSON-LD consistent. JSON-LD must be valid JSON and must not describe ratings, reviews, guarantees or features that the page cannot substantiate.
- Prefer direct answers, practical steps, real examples, explicit limitations and links to the relevant official application instructions. Keep application requirements date-sensitive and avoid presenting one portal's limits as a universal Indian standard.
- Do not add meta keywords, keyword-stuffed copy, near-duplicate pages, fake author credentials, fake reviews, or unverified third-party citation claims.
- Do not enforce a fixed minimum or maximum word count as an SEO rule. Page length alone is not a Google ranking target; keep enough content to solve the user's task clearly.
- Do not add llms.txt, special AI schema, FAQPage markup, or artificial text chunking as a supposed Google AI ranking shortcut. Google says standard search eligibility and helpful content remain the basis for its AI search features; no extra special schema is required.
- Treat Bing/Copilot eligibility and citations as dependent on crawlability, indexing, content quality and policy compliance. GEO improvements do not guarantee grounding or citation.

The homepage and seven task-specific guides already form the current topic cluster. Add another indexable page only when it answers a distinct user task with original, maintainable information.

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
