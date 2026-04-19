# Terraform-Specific Functions

This example shows:

- `encode_tfvars(...)`
- `decode_tfvars(...)`
- `encode_expr(...)`

Reference:

- `encode_tfvars` — https://developer.hashicorp.com/terraform/language/functions/terraform-encode_tfvars
- `decode_tfvars` — https://developer.hashicorp.com/terraform/language/functions/terraform-decode_tfvars
- `encode_expr` — https://developer.hashicorp.com/terraform/language/functions/terraform-encode_expr

## Files

- `tfvars_functions.py` — PHCL source
- `tfvars_functions.tf` — generated Terraform

## Rebuild

```bash
phcl build tfvars_functions.py
```

If `phcl` is not on your `PATH`:

```bash
python3 -m phcl build tfvars_functions.py
```

## Run

```bash
terraform init
terraform apply -auto-approve
```
