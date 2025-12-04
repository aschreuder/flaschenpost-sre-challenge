{{- define "shop_backend.name" -}}
shop_backend
{{- end }}

{{- define "shop_backend.fullname" -}}
{{- printf "%s-%s" .Release.Name "shop_backend" | trunc 63 | trimSuffix "-" -}}
{{- end }}

