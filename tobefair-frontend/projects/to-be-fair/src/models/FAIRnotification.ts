// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

export interface FAIRNotification {
  id: number;
  type: "error" | "info" | "info-square" | "warning" | "warning-alt" | "success";
  title: string;
  description: string;
  isOpen: boolean;
}
