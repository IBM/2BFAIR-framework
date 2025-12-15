// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { FAIRNotification } from "./FAIRnotification";

export interface FairnessEvaluation {
  evaluationId: string;

  evaluatedDigitalObjectID: string;
  evaluatedMetadataRecordID: string;
  evaluatedDigitalObjectLandingPageUrl: string;
  community: string;
  task: string;

  findability: number;
  accessibility: number;
  interoperability: number;
  reusability: number;
  totalScore: number;
  priorityRecommendations: Array<any>;

  detailedResults: any;

  evaluatedMetadata: any;

  notifications: Array<FAIRNotification>;
}
