{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "iwok8scollector.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 54 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 54 chars because some Kubernetes name fields are limited to 63 (by the DNS naming spec).
And the device connector will add the "pasadena-" prefix for a secret name.
If release name contains chart name it will be used as a full name.
*/}}
{{- define "iwok8scollector.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 54 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 54 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" $name .Release.Name | trunc 54 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "iwok8scollector.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 54 | trimSuffix "-" -}}
{{- end -}}
