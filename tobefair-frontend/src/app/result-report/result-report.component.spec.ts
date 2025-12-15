// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultReportComponent } from './result-report.component';

describe('ResultReportComponent', () => {
  let component: ResultReportComponent;
  let fixture: ComponentFixture<ResultReportComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ResultReportComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ResultReportComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
