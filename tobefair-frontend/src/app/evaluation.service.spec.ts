// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { TestBed } from '@angular/core/testing';

import { EvaluationService } from '../../projects/to-be-fair/src/lib/evaluation.service';

describe('EvaluationService', () => {
  let service: EvaluationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EvaluationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
