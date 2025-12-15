import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToBeFairComponent } from './to-be-fair.component';

describe('ToBeFairComponent', () => {
  let component: ToBeFairComponent;
  let fixture: ComponentFixture<ToBeFairComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ToBeFairComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ToBeFairComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
