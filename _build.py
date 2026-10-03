"""Builds the Mental Health Tools LLC website into this folder.

Run:  python3 _build.py

Edit the values below and rerun. Files starting with "_" are not published
by GitHub Pages.
"""
import os

# The owner chose to list only the state (27 Sep 2026). Apple and D&B don't
# require a street address or phone on the website: the D-U-N-S application
# carries the full address, and Apple's Support URL rule is "an easy way to
# contact you", which the support email satisfies.
LOCATION = "New Jersey, United States"

LEGAL_NAME = "Mental Health Tools LLC"
EMAIL = "support@mentalhealthtools.net"
UPDATED = "September 27, 2026"

HERE = os.path.dirname(os.path.abspath(__file__))

MAIL = f'<a href="mailto:{EMAIL}">support@<wbr>mentalhealthtools.net</a>'

MARK = ('<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><rect x="2" y="2" width="28" height="28" rx="8" '
        'fill="none" stroke="currentColor" stroke-width="3"/><circle cx="16" cy="16" r="5" fill="currentColor"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect x='2' y='2' "
           "width='28' height='28' rx='8' fill='none' stroke='%231D4F91' stroke-width='3'/%3E%3Ccircle cx='16' cy='16' "
           "r='5' fill='%231D4F91'/%3E%3C/svg%3E")
DROP = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" '
        'stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>')

CRISIS = ('If you are in crisis, including thoughts of suicide or self-harm or a crisis involving alcohol or drugs, '
          'call or text <a href="tel:988">988</a> or chat at <a href="https://988lifeline.org">988lifeline.org</a> '
          '(988 Suicide &amp; Crisis Lifeline, US). In an emergency, call 911.')


def page(title, description, current, body):
    def tab(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{FAVICON}">
<meta name="theme-color" content="#FFFFFF">
<link rel="stylesheet" href="/fonts/fonts.css">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap top-row">
    <a class="brand" href="/">{MARK}<span>{LEGAL_NAME}</span></a>
    <nav class="tabs" aria-label="Main">
      {tab("/", "Home", "home")}
      {tab("/products/", "Products", "products")}
      {tab("/contact/", "Contact", "contact")}
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap foot-row">
    <div>
      <p class="foot-name">&copy; 2026 {LEGAL_NAME}</p>
      <p>{LOCATION}</p>
    </div>
    <nav aria-label="Footer">
      <a href="/products/">Products</a>
      <a href="/contact/">Contact</a>
      <a href="/privacy/">Privacy</a>
      <a href="/terms/">Terms</a>
    </nav>
  </div>
</footer>
</body>
</html>
'''


def company_details():
    return f'''<dl class="details">
      <div><dt>Legal name</dt><dd>{LEGAL_NAME}</dd></div>
      <div><dt>Business type</dt><dd>Limited liability company</dd></div>
      <div><dt>Registered in</dt><dd>New Jersey, United States</dd></div>
      <div><dt>Founded</dt><dd>2026</dd></div>
      <div><dt>Email</dt><dd>{MAIL}</dd></div>
    </dl>'''


CLEARDAY_SUMMARY = f'''<article class="product">
      <div class="product-icon">{DROP}</div>
      <div class="product-body">
        <h3 class="product-name">Clearday</h3>
        <p class="product-tag">A self-help app for anyone who wants to cut back on or quit cannabis, alcohol, nicotine, vaping or stimulants, at their own pace.</p>
        <p class="meta"><span class="badge">Coming soon</span> iPhone &middot; Free 3-day trial, then a subscription</p>
        <a class="more" href="/products/clearday/">Clearday details and support</a>
      </div>
    </article>'''

HOME = page(LEGAL_NAME,
  f"{LEGAL_NAME} is a New Jersey software company that develops self-help mobile apps for reflection and everyday wellbeing.",
  "home", f'''
<section class="hero">
  <div class="wrap">
    <h1>{LEGAL_NAME}</h1>
    <p class="lede">We develop self-help mobile apps for reflection and everyday wellbeing.</p>
    <div class="actions">
      <a class="btn" href="/products/">View our products</a>
      <a class="btn btn-quiet" href="/contact/">Contact us</a>
    </div>
  </div>
</section>

<section class="block" aria-labelledby="about">
  <div class="wrap grid-2">
    <div>
      <h2 id="about">About the company</h2>
      <p>{LEGAL_NAME} is a software company based in New Jersey, founded in 2026. We design and publish mobile apps that help people reflect on their habits and make changes at their own pace.</p>
      <p>Our apps are self-help tools. They support reflection and habit change, and they are not therapy, medical care, or a substitute for a professional.</p>
    </div>
    <div class="panel">
      <h2 class="panel-title">Company details</h2>
      {company_details()}
    </div>
  </div>
</section>

<section class="block alt" aria-labelledby="products">
  <div class="wrap">
    <h2 id="products">Products</h2>
    {CLEARDAY_SUMMARY}
  </div>
</section>

<section class="block" aria-labelledby="commit">
  <div class="wrap">
    <h2 id="commit">Our commitments</h2>
    <div class="grid-3">
      <div><h3>No ads, no data selling</h3><p>Our apps don't show advertising or use third-party analytics, and we never sell, rent or trade personal information.</p></div>
      <div><h3>You control your data</h3><p>You can delete your account and everything stored in it yourself, at any time, from inside the app.</p></div>
      <div><h3>Self-help, not therapy</h3><p>Our apps don't diagnose or treat any condition and are not a substitute for professional care.</p></div>
    </div>
  </div>
</section>

<section class="note" aria-label="Crisis resources">
  <div class="wrap"><p>{CRISIS}</p></div>
</section>
''')

PRODUCTS = page(f"Products · {LEGAL_NAME}",
  f"Apps developed and published by {LEGAL_NAME}.",
  "products", f'''
<section class="page-head">
  <div class="wrap">
    <h1>Products</h1>
    <p class="lede">Apps developed and published by {LEGAL_NAME}.</p>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    {CLEARDAY_SUMMARY}
  </div>
</section>
''')

CLEARDAY = page(f"Clearday · {LEGAL_NAME}",
  "Clearday is a self-help app for anyone who wants to cut back on or quit cannabis, alcohol, nicotine, vaping or stimulants, at their own pace. Coming soon to iPhone.",
  "products", f'''
<section class="page-head">
  <div class="wrap">
    <p class="crumb"><a href="/products/">Products</a> / Clearday</p>
    <div class="app-head">
      <div class="product-icon large">{DROP}</div>
      <div>
        <h1 class="app-name">Clearday</h1>
        <p class="lede">A self-help app for anyone who wants to cut back on or quit cannabis, alcohol, nicotine, vaping or stimulants, at their own pace.</p>
        <p class="meta"><span class="badge">Coming soon</span> iPhone &middot; Free 3-day trial, then a subscription. SOS for cravings is always free.</p>
      </div>
    </div>
  </div>
</section>

<section class="block tight" aria-labelledby="features">
  <div class="wrap">
    <h2 id="features">Features</h2>
    <div class="grid-2 cards">
      <div class="card"><h3>Daily Reflections</h3><p>A short AI-guided reflection each day that helps you notice your patterns and choose one small experiment to try tomorrow. The AI is a self-reflection tool, not a therapist or a person.</p></div>
      <div class="card"><h3>SOS for cravings</h3><p>When an urge hits, tap SOS. Mark where you are on the craving wave, then ride it out with guided breathing, a reminder of your own reasons, or something to do. Skills you've practiced join your SOS toolkit.</p></div>
      <div class="card"><h3>Check-ins and progress</h3><p>Log your cravings and how much you cut back. Each check-in banks the share you cut back, so a day you cut back by half counts as half a day of progress.</p></div>
      <div class="card"><h3>Skills library</h3><p>Practice short skills for cravings and stress, like breathing, grounding and urge surfing. Pin your three favorites, and make if-then plans for the moments that tend to be hardest.</p></div>
    </div>
  </div>
</section>

<section class="block" aria-labelledby="privacy">
  <div class="wrap grid-2">
    <div>
      <h2 id="privacy">Privacy</h2>
      <ul class="list">
        <li>No advertising, no third-party analytics, no ad identifiers</li>
        <li>We never sell, rent or trade your information</li>
        <li>Reflections replies are written by an AI provider, Anthropic. It receives your messages and the progress details needed to reply, and does not use them to train its models</li>
        <li>Delete your account and everything stored in it yourself, any time</li>
        <li>Clearday's full privacy policy will be published here before launch</li>
      </ul>
    </div>
    <div>
      <h2>Before you start</h2>
      <ul class="list">
        <li>Clearday is a self-help app. It is not therapy, medical care or treatment, and it is not for emergencies</li>
        <li>If you drink heavily or every day, stopping suddenly can cause dangerous withdrawal, including seizures. Talk to a clinician before you stop or cut back sharply</li>
      </ul>
    </div>
  </div>
</section>

<section class="block alt" id="support" aria-labelledby="support-h">
  <div class="wrap grid-2">
    <div>
      <h2 id="support-h">Support</h2>
      <p>For questions about Clearday, your account, or your data, contact us:</p>
      {company_details()}
    </div>
    <div>
      <h2>Delete your account</h2>
      <p>Open Clearday, go to <b>You</b> &rsaquo; <b>Privacy &amp; data</b>, tap <b>Delete my account</b>, and confirm with your password. This permanently erases your account and everything stored in it.</p>
    </div>
  </div>
</section>

<section class="note" aria-label="Crisis resources">
  <div class="wrap"><p>{CRISIS}</p></div>
</section>
''')

CONTACT = page(f"Contact · {LEGAL_NAME}",
  f"Contact {LEGAL_NAME} by email.",
  "contact", f'''
<section class="page-head">
  <div class="wrap">
    <h1>Contact</h1>
    <p class="lede">For help with our apps, your account or your data, or any other question.</p>
  </div>
</section>
<section class="block tight">
  <div class="wrap">
    <div class="panel narrow">
      {company_details()}
    </div>
  </div>
</section>
''')

PRIVACY = page(f"Privacy · {LEGAL_NAME}",
  f"Privacy information for the {LEGAL_NAME} website.",
  "", f'''
<section class="page-head">
  <div class="wrap prose">
    <h1>Website privacy</h1>
    <p class="updated">Last updated {UPDATED}</p>
  </div>
</section>
<section class="block tight">
  <div class="wrap prose">
    <p>This page covers this website, mentalhealthtools.net. Each of our apps has its own privacy policy, linked below.</p>
    <h2>What this website collects</h2>
    <p>We don't collect anything through this website. It uses no cookies, analytics, advertising or tracking. Every file it loads, including the fonts, comes from mentalhealthtools.net itself, and pages make no requests to any other domain. If you follow a link to another site, that site's policy applies.</p>
    <p>This site is hosted on GitHub Pages, a service of GitHub, Inc. GitHub logs the IP address of visitors to GitHub Pages sites for security purposes, as described in the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a>. We don't receive or have access to those logs.</p>
    <h2>If you email us</h2>
    <p>We use your email address and message to reply and to handle what you ask for, such as a question about your Clearday account or data. Our email is hosted by Microsoft 365, which stores messages for us. We don't add you to a mailing list, and we don't sell or share your message with anyone else.</p>
    <h2>Our apps</h2>
    <ul class="list"><li>Clearday: its privacy policy will be published on this site before the app launches.</li></ul>
    <h2>Contact</h2>
    <p>{LEGAL_NAME}, {LOCATION}. {MAIL}</p>
  </div>
</section>
''')

TERMS = page(f"Terms · {LEGAL_NAME}",
  f"Terms of use for the {LEGAL_NAME} website.",
  "", f'''
<section class="page-head">
  <div class="wrap prose">
    <h1>Website terms of use</h1>
    <p class="updated">Last updated {UPDATED}</p>
  </div>
</section>
<section class="block tight">
  <div class="wrap prose">
    <p>These terms cover your use of this website, mentalhealthtools.net, operated by {LEGAL_NAME}. By using the site, you agree to them.</p>
    <h2>Information only</h2>
    <p>This website describes our company and our apps. Nothing on it is medical, psychological or legal advice, and it is not a substitute for a qualified professional. {CRISIS}</p>
    <h2>Our apps</h2>
    <p>Each app is governed by its own terms and privacy policy, which are presented in the app and on its App Store listing.</p>
    <h2>Content</h2>
    <p>The text, graphics and logos on this site belong to {LEGAL_NAME}. You may view and share links to the site, but you may not copy or reuse its content for commercial purposes without our permission.</p>
    <h2>No warranty</h2>
    <p>The site is provided "as is." We work to keep it accurate and available, but we don't guarantee that it is error-free or always online. To the extent the law allows, {LEGAL_NAME} is not liable for damages arising from your use of this website.</p>
    <h2>Governing law</h2>
    <p>These terms are governed by the laws of the State of New Jersey, United States.</p>
    <h2>Changes</h2>
    <p>We may update these terms. The date at the top shows when they last changed.</p>
    <h2>Contact</h2>
    <p>{LEGAL_NAME}, {LOCATION}. {MAIL}</p>
  </div>
</section>
''')

NOT_FOUND = page(f"Page not found · {LEGAL_NAME}", "This page could not be found.", "", f'''
<section class="page-head">
  <div class="wrap">
    <h1>Page not found</h1>
    <p class="lede">That page doesn't exist. Try the <a href="/">home page</a> or our <a href="/products/">products</a>.</p>
  </div>
</section>
''')

FILES = {
    "index.html": HOME, "products/index.html": PRODUCTS, "products/clearday/index.html": CLEARDAY,
    "contact/index.html": CONTACT, "privacy/index.html": PRIVACY, "terms/index.html": TERMS,
    "404.html": NOT_FOUND, "CNAME": "mentalhealthtools.net\n",
}
for rel, content in FILES.items():
    path = os.path.join(HERE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"built {len(FILES)} files")
