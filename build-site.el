(require 'ox-publish)
(setq org-publish-project-alist
      '(("org-notes"
         :base-directory "."
         :base-extension "org"
         :publishing-directory "./publish"
         :recursive t
         :publishing-function org-html-publish-to-html
         :headline-levels 2             ; Just the default for this project.
         :auto-sitemap t                ; Generate sitemap.org automagically...
         :sitemap-filename "sitemap.org"  ; ... call it sitemap.org (it's the default)...
         :sitemap-title "Sitemap"         ; ... with title 'Sitemap'.
         :auto-preamble t)

        ("org-static"
         :base-directory "."
         :base-extension "css\\|js\\|png\\|jpg\\|gif\\|pdf\\|mp3\\|ogg\\|swf"
         :publishing-directory "./files"
         :recursive t
         :publishing-function org-publish-attachment)
        ("org" :components ("org-notes" "org-static"))
        ))


;; Customize the HTML output
(setq org-html-validation-link nil            ;; Don't show validation link
      org-html-head-include-scripts nil       ;; Use our own scripts
      org-html-head-include-default-style nil ;; Use our own styles
      ;; org-html-head "<link rel=\"stylesheet\" href=\"https://cdn.simplecss.org/simple.min.css\" />"
      )

;; Generate the site output
(org-publish-all t)
(message "Build complete!")
