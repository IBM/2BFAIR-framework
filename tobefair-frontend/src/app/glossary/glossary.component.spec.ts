// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GlossaryComponent } from './glossary.component';

describe('GlossaryComponent', () => {
  let component: GlossaryComponent;
  let fixture: ComponentFixture<GlossaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GlossaryComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(GlossaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
