# Changelog

## v0.1.4

- Aligned the Terraform dialect with `phcl` `0.2.2`
- Fixed rendering for unlabeled `terraform {}` and `locals {}` blocks
- Fixed rendering for single-label `provider "aws" {}` blocks
- Added dialect coverage for Terraform auto-label behavior

## v0.1.3

- Removed Terraform-specific `for_each` iterable auto-normalization
- Removed redundant `@abstract` decorators from Terraform root declaration types

## v0.1.2

- Added PHCL `0.2.0` compatibility fixes
- Updated the minimum `phcl` dependency to `>=0.2.0`
- Moved example imports to `phcl.syntax`

## v0.1.1

- Initial PHCL Terraform dialect release
- Added Terraform-shaped declaration roots
- Added Terraform traversal helpers: `each`, `var`, `local`, and `module`
- Added `TerraformPHCL` default file config base
- Added dialect test suite
