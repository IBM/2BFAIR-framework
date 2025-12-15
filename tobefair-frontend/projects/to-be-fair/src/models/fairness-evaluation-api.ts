// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { FAIRNotification } from "./FAIRnotification";

export interface FairnessEvaluationAPI {
  overall_result: {
    evaluation_id: string;
    evaluated_digital_object_id: string;
    evaluated_metadata_record_id: string;
    task: string;
    community: string;
    evaluated_digital_object_landing_page_url: string;
    evaluation_score: {
      Findability: number;
      Accessibility: number;
      Interoperability: number;
      Reusability: number;
      total_score: number;
    };
    priority_recommendations: Array<any>;
  };

  detailed_results: any;

  evaluated_metadata: any;

  notifications: Array<FAIRNotification>;
}
