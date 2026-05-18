# optimalx-group.github.io

## Development Setup

This website is built using Jekyll and deployed via GitHub Pages. We use Ruby and Bundler to manage dependencies.

To **deploy changes**, simply commit and push to the repository. GitHub Pages will automatically rebuild and publish the site.

The steps below are for **editing and previewing the site locally** before pushing.

### Run the site locally

Install dependencies and start the local server:

```bash
bundle install
bundle exec jekyll serve
```

The site will be available at:

http://127.0.0.1:4000

### Editing the website

#### Posts

All blog posts are located in the `_posts/` directory and written in Markdown. Each post includes a YAML header with metadata such as title, description, and category.

#### People

Lab members are listed in the `_people/` directory. Each entry is a Markdown file describing the person's profile and role.

#### Publications

Publications are managed in `publications.md` and BibTeX files in `_bibliography/`.

#### News

Front page news items are maintained in `_data/news.yml`.

### Notes

- This site is built with Jekyll and hosted on GitHub Pages
- Changes are automatically deployed after pushing to the repository
- The site is based on a fork of the Kording Lab website template
