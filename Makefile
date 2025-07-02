release:
	@# Ensure VERSION is provided and follows the correct format
	@if [ -z "$(VERSION)" ]; then echo "Error: VERSION is not set. Please use VERSION=vX.Y.Z format."; exit 1; fi
	@if ! echo $(VERSION) | grep -Eq '^v[0-9]+\.[0-9]+\.[0-9]+$$'; then echo "Error: VERSION must be in format vX.Y.Z"; exit 1; fi

	@# Strip the 'v' prefix for use in __version__ and CITATION.cff fields
	$(eval VERSION_STRIPPED := $(shell echo $(VERSION) | sed 's/^v//'))

	@# 1. Generate changelog using git-cliff and prepend to CHANGELOG.md
	@git cliff -t $(VERSION) --unreleased --prepend CHANGELOG.md

	@# 2. Update version in src/__init__.py
	@sed -i '' 's/__version__ = .*/__version__ = "$(VERSION_STRIPPED)"/' src/__init__.py

	@# Confirm release preparation
	@echo "Release $(VERSION) prepared successfully."

	@# Display hint to create commit and tag
	@echo "--------------------------------------------------"
	@echo "To finalize the release, please commit the changes:"
	@echo "    git add CHANGELOG.md src/__init__.py"
	@echo "    git commit -m 'chore: release $(VERSION)'"
	@echo "    git tag $(VERSION)"
	@echo "    git push origin main --tags"
	@echo "--------------------------------------------------"
