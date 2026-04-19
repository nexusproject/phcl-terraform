# AWS Basic

This example shows a small Terraform-shaped PHCL file that defines:

- `terraform {}`
- `provider "aws" {}`
- `resource "aws_ecr_repository" {}`
- nested Terraform blocks via `B(...)`
- an output

## Files

- `aws_basic.py` — PHCL source
- `aws_basic.tf` — generated Terraform

## Rebuild

```bash
phcl build aws_basic.py
```

If `phcl` is not on your `PATH`:

```bash
python3 -m phcl build aws_basic.py
```
