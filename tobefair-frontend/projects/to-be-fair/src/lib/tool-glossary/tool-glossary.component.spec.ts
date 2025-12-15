import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolGlossaryComponent } from './tool-glossary.component';

describe('ToolGlossaryComponent', () => {
  let component: ToolGlossaryComponent;
  let fixture: ComponentFixture<ToolGlossaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ToolGlossaryComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ToolGlossaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
