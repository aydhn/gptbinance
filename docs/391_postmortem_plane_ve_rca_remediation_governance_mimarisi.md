# Phase 77: Postmortem Plane ve RCA Remediation Governance Mimarisi

Bu dokuman incidents -> causes -> actions -> verification -> debt/recurrence -> closure akışını anlatır.

## Neden Symptom != Cause != Verified Fix?
Çünkü semptomlar (örneğin timeout) sadece tetikleyicidir. Proximate cause veritabanı kilitlenmesidir, ama root cause eksik index veya kontrolsüz retry fırtınasıdır. Düzeltme (corrective action) timeout süresini uzatmak olabilir ama preventive action retry mekanizmasına backoff eklemek ve index oluşturmaktır. Doğrulanmayan (verified) action ise sadece bir "dilek"tir, remediation değildir.

## Neden Blame-Only RCA Yasak?
İnsan hatası (human error) tek başına bir root cause olamaz. Sistem bu hataya nasıl izin verdi? Hangi safeguard eksikti? Automation gap var mıydı? Blame-only RCA, gerçek root cause'u gizler ve organizasyonel debt'i (debt burial) artırır.
