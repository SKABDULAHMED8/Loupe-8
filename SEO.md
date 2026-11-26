# Loupe-8 SEO, AEO and GEO operating notes

## Product and primary search intent

Loupe-8 is a free browser-based image resizer, compressor, cropper and format converter. It helps users prepare existing JPG, PNG, WebP and GIF images for online forms, documents, profiles and other uploads.

Primary task cluster:
- Resize an image to exact pixel dimensions.
- Reduce a JPG or WebP image to a maximum KB limit.
- Crop an existing photo to a required frame or aspect ratio.
- Resize a scanned signature image for an application.
- Convert JPG, PNG and WebP files.
- Prepare a profile picture or an application photo using requirements published by the destination service.

The homepage is the main application page. The new online-form guide explains the decision between exact dimensions and maximum file size. Other guides support distinct tasks. Do not create many near-duplicate pages for small keyword variations.

## Current deployment

- Live URL: https://skabdulahmed8.github.io/Loupe-8/
- Canonical URL: https://skabdulahmed8.github.io/Loupe-8/
- Sitemap: https://skabdulahmed8.github.io/Loupe-8/sitemap.xml
- The repository contains a project-path robots file at /Loupe-8/robots.txt. It is not the origin-root robots policy.
- Checked on 26 November 2026: https://skabdulahmed8.github.io/robots.txt returned 404. That means no explicit origin-root robots directives were published at that address; it is not evidence that crawlers are blocked.
- A project-subpath repository cannot set the origin-root robots policy for all of github.io. Do not claim that its nested robots.txt controls Googlebot or AI search crawlers across the host.
- A custom domain gives Loupe-8 its own origin and allows a domain-root robots.txt. Treat a domain migration as a separate project with redirects, canonical changes and a migration checklist.

## Search appearance

- Homepage title: Free Online Image Resizer: Exact Pixels & KB Limits | Loupe-8
- Homepage H1: Free online image resizer for exact pixels and KB limits
- The title and description describe the product category and the tasks. Google may rewrite title links and snippets.
- Keep canonical URLs, Open Graph URLs, Twitter metadata, internal links and sitemap URLs aligned.
- The existing social image is LOUPE_Home_Logo1.png, 2146 × 733. It is a wide logo, not a purpose-built 1200 × 630 share card.

## Baseline visibility snapshot — 26 November 2026

These are observed query checks, not a full indexing report:
- Google query: site:skabdulahmed8.github.io/Loupe-8/ returned zero visible URLs.
- Google generic query: free online image resizer exact pixel dimensions returned no Loupe-8 result in the first 20 visible organic results.
- Google generic query: compress image to 20KB or 50KB online for form upload returned no Loupe-8 result in the first 20 visible organic results.
- Six related generic-intent queries tested with Tavily returned no Loupe-8 result in their first ten results.

A zero-result site: query is a warning signal, not a substitute for Google Search Console. There is no verified Search Console Page Indexing report, URL Inspection result, Bing index report, search impression data or traffic data in this audit. Do not claim that all pages are indexed or that rankings have improved until those data are available.

## Product behavior: describe accurately

- Input formats: JPG, PNG, WebP and GIF. Animated GIF input is processed as one still image.
- Output formats: JPG, PNG and WebP.
- Compress mode searches for the best JPG or WebP quality under the chosen maximum. If needed, it also reduces pixel dimensions. The result can be smaller than the maximum.
- Resize mode sets the target pixel dimensions. With a maximum KB value, it tries to reach the limit by reducing quality while keeping those dimensions. If it cannot meet both requirements, it shows a warning; the user must reduce dimensions or use a larger maximum only if the application permits it.
- Crop mode supports common aspect ratios and lets the user position the crop.
- The minimum file-size option applies to JPG output and may add non-image data to reach the requested file length. It does not improve visible quality. Users should use it only when the form explicitly has a minimum.
- DPI metadata is written to JPG output only.
- The selected image is processed in the browser and is not uploaded to a Loupe image-processing server. The page loads Google Fonts; the hosting provider may retain standard server logs.
- Loupe-8 does not remove backgrounds, create a digital signature, validate an application or guarantee acceptance by a portal.

## India-first accuracy

- Application image limits vary by authority, service, examination, notification and year.
- Never present 35:45, 20 KB, 50 KB, 200 × 230 px or any preset as a universal official requirement.
- The 35:45 setting is a crop ratio, not a promise that an image meets a specific passport or recruitment specification.
- Check live official sources before publishing exact application requirements:
  - SSC: https://ssc.gov.in/
  - UPSC online application FAQ: https://upsconline.gov.in/OTRP/candidate/faq.php
  - Passport Seva: https://passportindia.gov.in/psp/apply
- State when an example comes from one authority only. Do not imply that one authority's values apply to another.

## Structured data

- Homepage: WebSite, Organization and WebApplication.
- Guide pages: Article and visible BreadcrumbList.
- Guide index: CollectionPage.
- JSON-LD must match visible page content and all JSON blocks must parse.
- Do not publish aggregateRating: ratings and reviews are local to each visitor's browser and are not a verifiable public aggregate.
- Do not add FAQPage markup for the purpose of seeking Google FAQ rich results.
- Do not add schema types or claims that do not match visible functionality.

## Search crawlers and AI answer engines

The crawler policy differs by provider and purpose:
- Google Search uses Googlebot. Google-Extended is a separate control for specified Gemini/AI training and grounding uses; it does not control inclusion in Google Search.
- ChatGPT Search uses OAI-SearchBot for search discovery. GPTBot is a separate training crawler.
- Anthropic lists Claude-SearchBot for search discovery and ClaudeBot for training collection.
- Perplexity uses PerplexityBot for search discovery.
- Bingbot supports Bing Search and Copilot discovery/grounding.

The site currently has no origin-root robots.txt at github.io, so this project cannot set crawler-specific rules at the origin root. Verify crawler policies only after using a dedicated domain or controlling the root Pages site. Allowing a crawler makes a page eligible to be fetched; it does not guarantee that a search engine or model will cite or rank the page.

Google's current AI search guidance says that normal SEO fundamentals, crawlability, clear content and unique people-first value remain important. Do not add llms.txt, special AI schema, forced chunking, keyword-stuffed FAQs or artificial brand mentions as ranking tricks. Do not manufacture third-party citations or reviews.

## Measurement plan

Keep the search baseline and date with each major release. Test the same prompt pool across Google, Bing, ChatGPT Search, Claude web search, Gemini and Perplexity:
- free online image resizer exact pixels
- resize image to exact width and height online
- compress JPG to maximum 50 KB online
- resize photo and scanned signature for an online application
- browser-based image resizer that does not upload the image to its own image-processing server
- convert JPG to PNG or WebP online

Record whether Loupe-8 is mentioned, whether its website is linked, which competing tools appear, and the exact query and date. Use a share-of-mentions percentage only after repeated, comparable tests. Do not infer AI citation share from ordinary search-engine ranking.

For Google, verify the URL-prefix property in Search Console, inspect the homepage and each canonical guide, submit the sitemap and review the Page Indexing and Performance reports. For Bing, verify the site in Bing Webmaster Tools and inspect indexing and AI Performance data where available. Sitemap submission and indexing requests are discovery signals, not guarantees.

## Canonical content cluster

- Homepage: https://skabdulahmed8.github.io/Loupe-8/
- Guide index: https://skabdulahmed8.github.io/Loupe-8/guides/
- Online-form image preparation: https://skabdulahmed8.github.io/Loupe-8/guides/prepare-image-for-online-form/
- Passport-style photo: https://skabdulahmed8.github.io/Loupe-8/guides/passport-photo-for-online-forms/
- Scanned signature: https://skabdulahmed8.github.io/Loupe-8/guides/signature-image-for-online-forms/
- 20 KB / 50 KB compression: https://skabdulahmed8.github.io/Loupe-8/guides/compress-image-to-20kb-or-50kb/
- Exact pixel resizing: https://skabdulahmed8.github.io/Loupe-8/guides/resize-image-to-exact-pixels/
- Profile-picture crop: https://skabdulahmed8.github.io/Loupe-8/guides/profile-photo-resizer/

## Maintenance

- Run python3 scripts/validate-static-assets.py before deployment.
- Check that every canonical page appears in sitemap.xml and has an internal link.
- Validate JSON-LD with the Schema Markup Validator and test relevant Google rich-result eligibility.
- Use Search Console and Bing Webmaster Tools for indexation evidence; do not treat a successful deployment as proof of indexation.
- Recheck PageSpeed on mobile and desktop after changes to images, fonts or layout.
- Recheck social previews after updating the share image.
